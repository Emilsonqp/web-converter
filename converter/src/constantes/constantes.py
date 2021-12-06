from enum import Enum


class AudioFormat(Enum):
    MP3 = 'mp3'
    ACC = 'acc'
    OGG = 'ogg'
    WAV = 'wav'
    WMA = 'wma'

    @staticmethod
    def all():
        return [a.value for a in AudioFormat]


class AudioContentType(Enum):
    MP3 = 'audio/mpeg'
    ACC = 'audio/aac'
    ACC2 = 'audio/aacp'
    OGG = 'audio/ogg'
    WAV = 'audio/vnd.wave'
    WAV2 = 'audio/wav'
    WAV3 = 'audio/wave'
    WAV4 = 'audio/x-wav'
    WMA = 'audio/x-ms-wma'

    @staticmethod
    def all():
        return [a.value for a in AudioContentType]


class TaskStatus(Enum):
    UPLOADED = 'uploaded'
    PROCESSED = 'processed'

class S3CustomKeys(Enum):
    AWS_ACCESS_KEY_ID = 'ASIAWRNPKSN4TCUFD5FA'
    AWS_SECRET_ACCESS_KEY = 'd+oNK/Dz6WvlCc/zZvPAc56SL/8HkSq7JQDLcXuf'
    AWS_SESSION_TOKEN = 'FwoGZXIvYXdzELr//////////wEaDHTyPipSq4GLdMY+qCLLAWvS6ax3i29MC1ZCFXDj42SBzfiA4iJK3QA+Aphttba4MFD3ZyniuwZ2SM7Imgu+PDirGaJLZcCNxa42qnyAyIgBRXTRTSpVhDeiRjIfZaiv8FfHpqV4KkFnfVpDrUu/L3tjG/NUH0VXRDgUjdlXJLuwh7c4gulnCNIBn/uUCYeq8y/iapBjSdWVdVxukGhmBNRCKLrCUjdQXsVUGr+AOgLTy4k1UEwp5fhC+0ZgQWFF0gkP5+cVpdPsehwrUIOAPTFcpvm56icsk8WLKJK5tY0GMi21CAkME7ceMpVZ+56O+ak9nwTdAEfVSPRlDpl5GrJBjctxWAd2OWjtleLVtRE='
