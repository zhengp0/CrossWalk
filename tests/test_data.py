# -*- coding: utf-8 -*-
"""
    test_data
    ~~~~~~~~~

    Test `data` model for `crosswalk` package.
"""
import numpy as np
import pandas as pd
import pytest
import crosswalk.data as data


# test case settings
num_obs = 5
num_covs = 3

@pytest.fixture()
def df():
    df = pd.DataFrame({
        'obs': np.random.randn(num_obs),
        'obs_se': np.random.rand(num_obs) + 0.01,
        'alt_dorms': np.arange(num_obs),
        'ref_dorms': np.arange(num_obs)[::-1],
        'study_id': np.array([2, 1, 2, 1, 3])
    })
    for i in range(num_covs):
        df['cov%i' % i] = np.random.randn(num_obs)
    return df


@pytest.mark.parametrize("study_id", [None, "study_id"])
def test_cwdata_study_id(df, study_id):
    cwdata = data.CWData(df,
                         'obs',
                         'obs_se',
                         'alt_dorms',
                         'ref_dorms',
                         covs=['cov%i' % i for i in range(num_covs)],
                         study_id=study_id)

    if study_id is not None:
        assert cwdata.num_studies == 3
        assert tuple(cwdata.study_sizes) == (2, 2, 1)
        assert tuple(cwdata.unique_study_id) == (1, 2, 3)
        assert tuple(cwdata.study_id) == (1, 1, 2, 2, 3)
    else:
        assert cwdata.num_studies == 5
        assert tuple(cwdata.study_sizes) == tuple([1]*num_obs)
        assert cwdata.unique_study_id is None


@pytest.mark.parametrize("study_id", [None, "study_id"])
@pytest.mark.parametrize("add_intercept", [True, False])
def test_cwdata_add_intercept(df, study_id, add_intercept):
    cwdata = data.CWData(df,
                         'obs',
                         'obs_se',
                         'alt_dorms',
                         'ref_dorms',
                         covs=['cov%i' % i for i in range(num_covs)],
                         study_id=study_id,
                         add_intercept=add_intercept)

    if add_intercept:
        assert "intercept" in cwdata.covs.columns
