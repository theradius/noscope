import inspect
import os
import shelve
import shutil
import tempfile


def save(key='default', persist=False):
    _init_save_path()
    f = _get_outer_frame()
    with shelve.open(_get_temp_path(str(key))) as db:
        if not persist:
            db.clear()
        _add_key_vals(db, f.frame.f_locals)
        _add_key_vals(db, f.frame.f_globals)


def load(key='default'):
    with shelve.open(_get_temp_path(str(key))) as db:
        f = _get_outer_frame()
        _add_key_vals(f.frame.f_globals, db)


def reset():
    shutil.rmtree(_get_save_path())


def _add_key_vals(to_dict, from_dict):
    for k in from_dict:
        try:
            to_dict[k] = from_dict[k]
        except TypeError:
            pass


def _get_outer_frame():
    stack = inspect.stack()
    for frame in stack:
        if frame.filename == __file__:
            continue
        return frame


def _get_save_path():
    return os.path.join(tempfile.gettempdir(), 'noscope')


def _init_save_path():
    save_path = _get_save_path()
    if not os.path.exists(save_path):
        os.makedirs(save_path)


def _get_temp_path(key):
    return os.path.join(_get_save_path(), 'noscope_state_' + key)
