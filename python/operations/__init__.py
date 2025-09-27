# setup
from operations.setup import SetupCoreDirectories

# create
from operations.create import CreateTmpNote

# editor
from operations.editor import EditWithNvim


operations = {
    "setup_core_directories": SetupCoreDirectories,
    "create_tmp_note": CreateTmpNote,
    "edit_with_nvim": EditWithNvim
}

