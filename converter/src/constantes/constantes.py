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
    AWS_ACCESS_KEY_ID = 'ASIAWRNPKSN4YEHBP4GW'
    AWS_SECRET_ACCESS_KEY = '8uMBGv2CSDQDVsBE2w29KCzEWJIG5ne1ysXJxwvJ'
    AWS_SESSION_TOKEN = 'FwoGZXIvYXdzEL7//////////wEaDLIZxS2SfgU0Xd8P5CLLAdE2hJvMGpGr1Elb6Cmz8PmYU25MR1ujQgCDzKaKLb3d/dnLUfhcDmVqXo5GC06Ib5h8EVeULhVZWH17Gf1nuFPw3fTsaJzKjtW0Id5oFurcvnJQ5jJPrSocUqzymCZPvSJ/MdcEb1stbLLHjwqc01xjgurNmW9Ld7mS9NcCtAMzfofCyWZcxDLcmVKsctrhupWXuOJ0jlDpagM21/B2lX55Zsw4gpPQIGbtMb/F9BLPMJM3M1mOyrjTwpx4XfiWgyeJD8l9poAUSEBKKNCxto0GMi16N7p4dP8v1YpFGuQoX4EI85ISaB+m2YYPjLJzkPZ52ylZBxJfRiYRuwWSnog='
