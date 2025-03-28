from .uav import UAVDataset
from .dtb import DTBDataset
from .uav10fps import UAV10Dataset
from .uav20l import UAV20Dataset
from .uavdt import UAVDTDataset
from .uavtrack112 import UAVTrack112Dataset
class DatasetFactory(object):
    @staticmethod
    def create_dataset(**kwargs):
        """
        Args:
            name: dataset name
            dataset_root: dataset root
            load_img: wether to load image
        Return:
            dataset
        """
        assert 'name' in kwargs, "should provide dataset name"
        name = kwargs['name']
        if 'DTB70' in name:
            dataset = DTBDataset(**kwargs)
        elif 'UAV123@10fps' in name:
            dataset = UAV10Dataset(**kwargs)
        elif 'UAV12320l' in name:
            dataset = UAV20Dataset(**kwargs)
        elif 'UAV123' in name:
            dataset = UAVDataset(**kwargs)
        elif 'UAVDT' == name:
            dataset = UAVDTDataset(**kwargs)
        elif 'UAVTrack112' == name:
            dataset = UAVTrack112Dataset(**kwargs)
        else:
            raise Exception("unknow dataset {}".format(kwargs['name']))
        return dataset

