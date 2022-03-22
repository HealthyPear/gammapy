# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Built-in models in Gammapy."""
from gammapy.utils.registry import Registry
from .core import Model, Models, DatasetModels, ModelBase
from .cube import (
    SkyModel, FoVBackgroundModel, TemplateNPredModel,
    create_fermi_isotropic_diffuse_model,
)
from .spatial import (
    SpatialModel,
    PointSpatialModel,
    GaussianSpatialModel,
    GeneralizedGaussianSpatialModel,
    DiskSpatialModel,
    ShellSpatialModel,
    Shell2SpatialModel,
    ConstantSpatialModel,
    ConstantFluxSpatialModel,
    TemplateSpatialModel,
)
from .spectral import (
    scale_plot_flux,
    integrate_spectrum,
    SpectralModel,
    ConstantSpectralModel,
    CompoundSpectralModel,
    PowerLawSpectralModel,
    PowerLawNormSpectralModel,
    PowerLaw2SpectralModel,
    BrokenPowerLawSpectralModel,
    SmoothBrokenPowerLawSpectralModel,
    PiecewiseNormSpectralModel,
    ExpCutoffPowerLawSpectralModel,
    ExpCutoffPowerLawNormSpectralModel,
    ExpCutoffPowerLaw3FGLSpectralModel,
    SuperExpCutoffPowerLaw3FGLSpectralModel,
    SuperExpCutoffPowerLaw4FGLDR3SpectralModel,
    SuperExpCutoffPowerLaw4FGLSpectralModel,
    LogParabolaSpectralModel,
    LogParabolaNormSpectralModel,
    TemplateSpectralModel,
    TemplateNDSpectralModel,
    ScaleSpectralModel,
    EBLAbsorptionNormSpectralModel,
    NaimaSpectralModel,
    GaussianSpectralModel,
)

from .spectral_cosmic_ray import create_cosmic_ray_spectral_model
from .spectral_crab import (
    MeyerCrabSpectralModel,
    create_crab_spectral_model,
)
from .temporal import (
    TemporalModel,
    ConstantTemporalModel,
    LinearTemporalModel,
    ExpDecayTemporalModel,
    GaussianTemporalModel,
    GeneralizedGaussianTemporalModel,
    LightCurveTemplateTemporalModel,
    PowerLawTemporalModel,
    SineTemporalModel,
)



__all__ = [
    "BrokenPowerLawSpectralModel",
    "CompoundSpectralModel",
    "ConstantFluxSpatialModel",
    "ConstantSpatialModel",
    "ConstantSpectralModel",
    "ConstantTemporalModel",
    "create_cosmic_ray_spectral_model",
    "create_crab_spectral_model",
    "create_fermi_isotropic_diffuse_model",
    "DatasetModels",
    "DiskSpatialModel",
    "EBLAbsorptionNormSpectralModel",
    "ExpCutoffPowerLaw3FGLSpectralModel",
    "ExpCutoffPowerLawNormSpectralModel",
    "ExpCutoffPowerLawSpectralModel",
    "ExpDecayTemporalModel",
    "FoVBackgroundModel",
    "GaussianSpatialModel",
    "GaussianSpectralModel",
    "GaussianTemporalModel",
    "GeneralizedGaussianSpatialModel",
    "GeneralizedGaussianTemporalModel",
    "integrate_spectrum",
    "LightCurveTemplateTemporalModel",
    "LinearTemporalModel",
    "LogParabolaNormSpectralModel",
    "LogParabolaSpectralModel",
    "MeyerCrabSpectralModel",
    "Model",
    "Models",
    "ModelBase",
    "MODEL_REGISTRY",
    "NaimaSpectralModel",
    "PiecewiseNormSpectralModel",
    "PointSpatialModel",
    "PowerLaw2SpectralModel",
    "PowerLawNormSpectralModel",
    "PowerLawSpectralModel",
    "PowerLawTemporalModel",
    "scale_plot_flux",
    "ScaleSpectralModel",
    "Shell2SpatialModel",
    "ShellSpatialModel",
    "SineTemporalModel",
    "SkyModel",
    "SmoothBrokenPowerLawSpectralModel",
    "SPATIAL_MODEL_REGISTRY",
    "SpatialModel",
    "SPECTRAL_MODEL_REGISTRY",
    "SpectralModel",
    "SuperExpCutoffPowerLaw3FGLSpectralModel",
    "SuperExpCutoffPowerLaw4FGLDR3SpectralModel",
    "SuperExpCutoffPowerLaw4FGLSpectralModel",
    "TemplateSpatialModel",
    "TemplateSpectralModel",
    "TemplateNDSpectralModel",
    "TemplateNPredModel",
    "TEMPORAL_MODEL_REGISTRY",
    "TemporalModel",
]


SPATIAL_MODEL_REGISTRY = Registry(
    [
        ConstantSpatialModel,
        TemplateSpatialModel,
        DiskSpatialModel,
        GaussianSpatialModel,
        GeneralizedGaussianSpatialModel,
        PointSpatialModel,
        ShellSpatialModel,
        Shell2SpatialModel,
    ]
)
"""Registry of spatial model classes."""

SPECTRAL_MODEL_REGISTRY = Registry(
    [
        ConstantSpectralModel,
        CompoundSpectralModel,
        PowerLawSpectralModel,
        PowerLaw2SpectralModel,
        BrokenPowerLawSpectralModel,
        SmoothBrokenPowerLawSpectralModel,
        PiecewiseNormSpectralModel,
        ExpCutoffPowerLawSpectralModel,
        ExpCutoffPowerLaw3FGLSpectralModel,
        SuperExpCutoffPowerLaw3FGLSpectralModel,
        SuperExpCutoffPowerLaw4FGLDR3SpectralModel,
        SuperExpCutoffPowerLaw4FGLSpectralModel,
        LogParabolaSpectralModel,
        TemplateSpectralModel,
        TemplateNDSpectralModel,
        GaussianSpectralModel,
        EBLAbsorptionNormSpectralModel,
        NaimaSpectralModel,
        ScaleSpectralModel,
        PowerLawNormSpectralModel,
        LogParabolaNormSpectralModel,
        ExpCutoffPowerLawNormSpectralModel,
    ]
)
"""Registry of spectral model classes."""

TEMPORAL_MODEL_REGISTRY = Registry(
    [
        ConstantTemporalModel,
        LinearTemporalModel,
        LightCurveTemplateTemporalModel,
        ExpDecayTemporalModel,
        GaussianTemporalModel,
        GeneralizedGaussianTemporalModel,
        PowerLawTemporalModel,
        SineTemporalModel,
    ]
)
"""Registry of temporal models classes."""

MODEL_REGISTRY = Registry([SkyModel, FoVBackgroundModel, TemplateNPredModel])
"""Registry of model classes"""
