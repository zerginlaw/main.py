# -*- coding: utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Bar
from Apriori import sup_data
# 假设数据已经处理好并存储在 data 中
data = sup_data
data = [(list(k), v) for k, v in data.items()]
data = sorted(data, key=lambda x: x[1], reverse=True)

bar = (
    Bar(opts.InitOpts(width='1300px',height='500px'))
    .add_xaxis([str(item[0]) for item in data])
    .add_yaxis("支持度", [item[1] for item in data], category_gap="50%")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Frequent Itemsets"),
        xaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(rotate=-15, font_size=10),

            name_location="middle"
        ),
        yaxis_opts=opts.AxisOpts(name="支持度")

    )
)
bar.render("frequent_itemsets.html")#
