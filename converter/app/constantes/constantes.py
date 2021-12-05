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
    AWS_ACCESS_KEY_ID = 'ASIAWRNPKSN4RCQYS47Q'
    AWS_SECRET_ACCESS_KEY = '2mg66vHR2It6LJfXY78LT8MCkbDNaTMmE6DYNy0o'
    AWS_SESSION_TOKEN = 'FwoGZXIvYXdzEHEaDILRnDwcXtG26LBnbCLLAc+ecR8PiOQ+7G9qsuqzz31Pbb+D96qlQ2qqdhnI7U4Trawlii+4fk+a5Km0ye+BqE/tv/M/c7xM14rNS0M0prw93CF72awgcJutv/gCrtPzezMCwygN/PMcMsmmo0v7ECCw00iWVQI44AQaPO/GKAlURDHSpuUkQbLJcUI0K+R+9u+3cn0FkWiy98reLbLx23gTXxVe4pvB2Bns11QiPh9KijR41CNXtQ0LJhZfdmMpquxqJ8OKD95aa7FnkiH+/Put3bRN0NvT2eolKPK7pY0GMi2TqVvRdLgDC/AeB3Ni0zHXiLDLoI5HQMrWgHVbgYfbSrbVx+bdq9wSYyauxF8='
