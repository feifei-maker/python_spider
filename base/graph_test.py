# @Time : 2020/9/3 10:15 
# @Author : fei_fei
# @File : graph_test.py 
# @Software: PyCharm
import plotly;


# 如果太长可以设置别名
# import plotly.graph_objs as go

def draw_line_graph():
    # 准备图轨数据
    trace_1 = plotly.graph_objs.Scatter(
        x=[1, 2, 3, 4],
        y=[10, 15, 13, 17],
        name="散点图",
        # 散点参数
        mode="markers"
    );
    trace_2 = plotly.graph_objs.Scatter(
        x=[1, 2, 3, 4],
        y=[16, 5, 11, 9],
        name="折线图",
        mode="lines"
    );
    line_data = [trace_1, trace_2];
    # 设置画图布局
    layout = plotly.graph_objs.Layout(title="折线图展示", xaxis={"title": "x"}, yaxis={"title": "y"});
    # 融合图轨数据和布局
    figure = plotly.graph_objs.Figure(data=line_data, layout=layout);
    # 生成图表和图片
    filepath = "E://python_production_projects/python_graph/line_graph.html";
    plotly.offline.plot(figure, filename=filepath, image="png");


def draw_bar_graph():
    # 准备图轨数据
    trace_1 = plotly.graph_objs.Bar(
        x=[1, 2, 3, 4],
        y=[32, 44, 11, 66],
        name="第一产业"
    );
    trace_2 = plotly.graph_objs.Bar(
        x=[1, 2, 3, 4],
        y=[36, 23, 18, 54],
        name="第二产业"
    );
    trace_3 = plotly.graph_objs.Bar(
        x=[1, 2, 3, 4],
        y=[54, 34, 26, 17],
        name="第三产业"
    );
    bar_data = [trace_1, trace_2, trace_3];

    # 设置画布布局
    layout = plotly.graph_objs.Layout(title="柱状图测试", xaxis={"title": "季度"}, yaxis={"title": "产值"});
    # 融合图轨数据和布局
    figure = plotly.graph_objs.Figure(data=bar_data, layout=layout);
    # 输出
    filepath = "E://python_production_projects/python_graph/bar_graph.html";
    plotly.offline.plot(figure, filename=filepath, image="png");


def draw_pie_graph():
    # 准备图轨数据
    trace_1 = plotly.graph_objs.Pie(
        labels=["产品一", "产品二", "产品三", "产品四", "产品五"],
        values=[13.4, 24.6, 33.2, 76.2, 65.5]
    );
    pie_data = [trace_1];

    # 设置画布布局
    layout = plotly.graph_objs.Layout(title="饼图测试");
    # 融合图轨数据和布局
    figure = plotly.graph_objs.Figure(data=pie_data, layout=layout);
    # 输出
    filepath = "E://python_production_projects/python_graph/pie_graph.html";
    plotly.offline.plot(figure, filename=filepath, image="png");


if __name__ == "__main__":
    draw_line_graph();
    draw_bar_graph();
    draw_pie_graph();