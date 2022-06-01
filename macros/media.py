from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {
    "name": "Media",
    "macros": [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, "", []),
        (0x000020, "Vol+", [[ConsumerControlCode.VOLUME_INCREMENT]]),
        (0x202020, "Bright+", [[ConsumerControlCode.BRIGHTNESS_INCREMENT]]),
        # 2nd row ----------
        (0x000000, "", []),
        (0x000020, "Vol-", [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x202020, "Bright-", [[ConsumerControlCode.BRIGHTNESS_DECREMENT]]),
        # 3rd row ----------
        (0x000000, "", []),
        (0x200000, "Mute", [[ConsumerControlCode.MUTE]]),
        (0x000000, "", []),
        # 4th row ----------
        (0x202000, "<<", [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),
        (0x002000, "Play/Pause", [[ConsumerControlCode.PLAY_PAUSE]]),
        (0x202000, ">>", [[ConsumerControlCode.SCAN_NEXT_TRACK]]),
        # Encoder button ---
        (0x000000, "", []),
    ],
}
