from behavioral.state import JiraTask, DefinedStatus


class TestState:
    def test_it_change_status_task(self):
        task = JiraTask(DefinedStatus())
        assert task.get_status() == 'defined'

        task.move()
        assert task.get_status() == 'in_progress'

        task.move()
        assert task.get_status() == 'in_review'

        task.move()
        assert task.get_status() == 'done'
