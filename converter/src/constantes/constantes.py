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
    AWS_ACCESS_KEY_ID = 'ASIAWRNPKSN4WDZCDCT3'
    AWS_SECRET_ACCESS_KEY = 'kNiQ9l6B/DXmXs4JRJY07bpMGQ2QscN93HDnLKwH'
    AWS_SESSION_TOKEN = 'FwoGZXIvYXdzELL//////////wEaDCof4zQCmYJyAsyhTCLLAceyh/Df/fdhw2QrBRzR2z6a+0MROmP6ZVcfyMZAXDwjkvwyEuY7kI9jheM/htk65asHrCyfGh8tl0xsDcHnpeYG2OanWMnltu0mSM3ETdCs4kg9ezye08gEBgi/w6tQ0H8jH57NE9RY4g8Qw6a7w8z7p2ZKDZct09hK2i4+kzU9c1P8uVf0FYUZ7ss7FOv9ZVJZUvPbVNnTk2fGRXFdY5J5octAoOKcLYp9H3DsJ3Rrr4ImDw6u/GpYLmF4ZxmdfBvJyud4r2hsp0OHKIjVs40GMi12mHWX/Q1NECzJutySk1l1pcPvxnbICa2hEce3D24ZJW6JTbMGXvR1IhTrxt4='
