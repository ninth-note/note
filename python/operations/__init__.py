# setup
from operations.setup import SetupCoreDirectories

# create
from operations.create import CreateNote, CreateTmpNote

# editor
from operations.edit import EditWithNvim


operations = {
    "setup_core_directories": SetupCoreDirectories,
    "create_note": CreateNote,
    "create_tmp_note": CreateTmpNote,
    "edit_with_nvim": EditWithNvim
}


