from abc import ABCMeta, abstractmethod


STATUS_DEFINED = 'defined'
STATUS_IN_PROGRESS = 'in_progress'
STATUS_REVIEW = 'in_review'
STATUS_DONE = 'done'


class TaskStatus(metaclass=ABCMeta):
    """
    Interface to encapsulate the behavior associated with a particular state of the JiraTask.
    """
    @abstractmethod
    def get_status_name(self):
        pass


class DefinedStatus(TaskStatus):
    """
    Behavior associated with defined state on a JiraTask.
    """
    def get_status_name(self):
        return STATUS_DEFINED


class InProgressStatus(TaskStatus):
    """
    Behavior associated with in progress state on a JiraTask.
    """
    def get_status_name(self):
        return STATUS_IN_PROGRESS


class InReviewStatus(TaskStatus):
    """
    Behavior associated with in review state on a JiraTask.
    """
    def get_status_name(self):
        return STATUS_REVIEW


class DoneStatus(TaskStatus):
    """
    Behavior associated with done state on a JiraTask.
    """
    def get_status_name(self):
        return STATUS_DONE


class JiraTask:
    """
    Context. Interface of interest to clients
    and it maintains an instance of a TaskStatus subclass that defines the current state.
    """
    def __init__(self, state):
        self._state = state

    def get_status(self):
        return self._state.get_status_name()

    def move(self):
        if self.get_status() == STATUS_DEFINED:
            self._state = InProgressStatus()
        elif self.get_status() == STATUS_IN_PROGRESS:
            self._state = InReviewStatus()
        elif self.get_status() == STATUS_REVIEW:
            self._state = DoneStatus()
