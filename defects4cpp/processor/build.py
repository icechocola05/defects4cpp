import lib
from lib import AssertFailed, ValidateFailed
from processor.actions import ActionRunner


def run_internal(action):
    try:
        action_runner = ActionRunner('d++ build --project=[project_name] --no=[number] [checkout directory]', action)
        succeed = action_runner.run()

        if not succeed:
            raise AssertFailed("Test Failed")
        else:
            lib.io.kindness_message("Completed")

    except ValidateFailed:
        lib.io.error_message("invalid arguments, check project name or bug numbers")
    except AssertFailed as e:
        lib.io.error_message(e)
    except SystemExit:
        pass
    except:
        lib.io.error_message(lib.get_trace_back())
        pass


def run_cov_build():
    run_internal('builder-cov')


def run_build():
    run_internal('builder')
