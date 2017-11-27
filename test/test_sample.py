from orminator import session_manager

from app import models

def test_delete_sample(session_class):
    """Test sample deletion also deletes sample attributes
    but not sample attribute types.
    """
    with session_manager(session_class) as session:
        # create a sample with two attributes
        sample_attr_type_1 = session.query(models.Sample_attr_type).filter(
            models.Sample_attr_type.type_ == 'depth').one()
        sample_attr_type_2 = session.query(models.Sample_attr_type).filter(
            models.Sample_attr_type.type_ == 'pressure').one()

        sample_attr_1 = models.Sample_attr(sample_attr_type=sample_attr_type_1)
        sample_attr_1.value = 'test_delete_sample'
        sample_attr_2 = models.Sample_attr(sample_attr_type=sample_attr_type_2)
        sample_attr_2.value = 'test_delete_sample'

        sample = models.Sample(
            cast_number=999,
            collection_time_zone='HST',
            sample_name='test sample',
            station_number=999)
        sample.sample_attr_list.append(sample_attr_1)
        sample.sample_attr_list.append(sample_attr_2)

        sample_file_1 = models.Sample_file(
            file_='sample_file_1',
            sample_file_type_id=1)
        sample_file_2 = models.Sample_file(
            file_='sample_file_2',
            sample_file_type_id=1)

        sample.sample_file_list.append(sample_file_1)
        sample.sample_file_list.append(sample_file_2)

        session.add(sample)

        assert 1 == session.query(models.Sample).filter(
            models.Sample.sample_name == 'test sample').count()

        assert 1 == session.query(models.Sample_attr).join(
            models.Sample_attr_type).filter(
            models.Sample_attr_type.type_ == 'depth').filter(
            models.Sample_attr.value == 'test_delete_sample').count()

        assert 1 == session.query(models.Sample_attr).join(
            models.Sample_attr_type).filter(
            models.Sample_attr_type.type_ == 'pressure').filter(
            models.Sample_attr.value == 'test_delete_sample').count()

        assert 1 == session.query(models.Sample_file).filter(
            models.Sample_file.file_ == 'sample_file_1').count()

        assert 1 == session.query(models.Sample_file).filter(
            models.Sample_file.file_ == 'sample_file_2').count()

        # verify the sample exists and has two attributes
        test_sample = session.query(models.Sample).filter(
            models.Sample.sample_name == 'test sample').one()

        assert len(test_sample.sample_attr_list) == 2
        assert len(test_sample.sample_file_list) == 2

        # delete the sample
        session.delete(test_sample)

        # verfify the sample and both attributes have been deleted
        assert 0 == session.query(models.Sample).filter(
            models.Sample.sample_name == 'test sample').count()

        assert 0 == session.query(models.Sample_attr).join(
            models.Sample_attr_type).filter(
            models.Sample_attr_type.type_ == 'depth').filter(
            models.Sample_attr.value == 'test_delete_sample').count()

        assert 0 == session.query(models.Sample_attr).join(
            models.Sample_attr_type).filter(
            models.Sample_file_type.type_ == 'pressure').filter(
            models.Sample_attr.value == 'test_delete_sample').count()

        assert 0 == session.query(models.Sample_file).filter(
            models.Sample_file.file_ == 'sample_file_1').count()

        assert 0 == session.query(models.Sample_file).filter(
            models.Sample_file.file_ == 'sample_file_2').count()
