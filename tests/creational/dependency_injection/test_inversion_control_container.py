from creational.dependency_injection import Editors


class TestInversionControlContainer:
    def test_it_inject_service_to_write_file(self):
        file_editor = Editors.file_editor()
        file_editor.save()

        assert file_editor.writer.files_written == 1

    def test_it_inject_service_to_write_database(self):
        database_writer = Editors.database_editor()
        database_writer.save()
        database_writer.save()

        assert database_writer.writer.tables_written == 2
