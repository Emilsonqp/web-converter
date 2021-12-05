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
    AWS_ACCESS_KEY_ID = 'ASIAWRNPKSN4U6LSXPXP'
    AWS_SECRET_ACCESS_KEY = 'snyUqbcXMBjnOH/HvTUmrzHHGvUDB01eoZdYOU0K'
    AWS_SESSION_TOKEN = 'FwoGZXIvYXdzELb//////////wEaDDr1Q8usMBMb0x0noiLLAYzAyzf4cVlWdkah0rsOfn/MTQdGAE0CN7MctMn7R1aCD8GV1UyLYFkbEwYF11yCxpVxqxHSZ+iWxeL6w775NzrqeIqZ7LlZSDZSQ3gEX2PaZTEDt2p3TXo1jj5H46sZCdo7a5kd+8Wbl/bdudOnY5dgQk3tyEEkkW8KycFlxaDjTRLc7AvgZutGj6ZKBYGy8gYF/FGhPyR93xPlkehEjSHmTnOcEM98UhiTF+GZsT19Bc13ASMDLYTfM7KwWelUZfmFjlpJXr5GbezEKKnItI0GMi2bkGYHuErpEU/wtXnOJa9GwGsuNlsPuavNJt33B9eQPtdlv5axmmPLuVtNBmg='
