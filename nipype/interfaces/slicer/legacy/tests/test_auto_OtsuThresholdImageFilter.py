# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..filtering import OtsuThresholdImageFilter


def test_OtsuThresholdImageFilter_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputVolume=dict(
            argstr='%s',
            extensions=None,
            position=-2,
        ),
        insideValue=dict(argstr='--insideValue %d', ),
        numberOfBins=dict(argstr='--numberOfBins %d', ),
        outputVolume=dict(
            argstr='%s',
            hash_files=False,
            position=-1,
        ),
        outsideValue=dict(argstr='--outsideValue %d', ),
    )
    inputs = OtsuThresholdImageFilter.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_OtsuThresholdImageFilter_outputs():
    output_map = dict(outputVolume=dict(
        extensions=None,
        position=-1,
    ), )
    outputs = OtsuThresholdImageFilter.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
