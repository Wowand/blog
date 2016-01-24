import pandas as pd
from pandas_highcharts.core import serialize
from pandas.compat import StringIO

dat = """ts;A;C
2015-01-01 00:00:00;27451873;29956800;113"""

df = pd.read_csv(StringIO(dat), sep=';', index_col='ts', parse_dates='ts')

chart = serialize(df, render_to="my-chart", title="Test", kind="bar")