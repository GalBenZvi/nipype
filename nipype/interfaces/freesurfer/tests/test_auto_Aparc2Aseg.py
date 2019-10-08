# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import Aparc2Aseg


def test_Aparc2Aseg_inputs():
    input_map = dict(
        a2009s=dict(argstr='--a2009s', ),
        args=dict(argstr='%s', ),
        aseg=dict(
            argstr='--aseg %s',
            extensions=None,
        ),
        copy_inputs=dict(),
        ctxseg=dict(
            argstr='--ctxseg %s',
            extensions=None,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        filled=dict(extensions=None, ),
        hypo_wm=dict(argstr='--hypo-as-wm', ),
        label_wm=dict(argstr='--labelwm', ),
        lh_annotation=dict(
            extensions=None,
            mandatory=True,
        ),
        lh_pial=dict(
            extensions=None,
            mandatory=True,
        ),
        lh_ribbon=dict(
            extensions=None,
            mandatory=True,
        ),
        lh_white=dict(
            extensions=None,
            mandatory=True,
        ),
        out_file=dict(
            argstr='--o %s',
            extensions=None,
            mandatory=True,
        ),
        rh_annotation=dict(
            extensions=None,
            mandatory=True,
        ),
        rh_pial=dict(
            extensions=None,
            mandatory=True,
        ),
        rh_ribbon=dict(
            extensions=None,
            mandatory=True,
        ),
        rh_white=dict(
            extensions=None,
            mandatory=True,
        ),
        ribbon=dict(
            extensions=None,
            mandatory=True,
        ),
        rip_unknown=dict(argstr='--rip-unknown', ),
        subject_id=dict(
            argstr='--s %s',
            mandatory=True,
            usedefault=True,
        ),
        subjects_dir=dict(),
        volmask=dict(argstr='--volmask', ),
    )
    inputs = Aparc2Aseg.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Aparc2Aseg_outputs():
    output_map = dict(out_file=dict(
        argstr='%s',
        extensions=None,
    ), )
    outputs = Aparc2Aseg.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
