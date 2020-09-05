# @Time : 2020/9/5 9:45 
# @Author : fei_fei
# @File : news_gzbd_graph.py 
# @Software: PyCharm
import plotly,news_gzbd_storage;


def draw_graph(graph_typle):
    classname = None;
    graph_name = None;
    graph_data = news_gzbd_storage.get_storage_data();
    district = graph_data.get("district");
    if graph_typle == "饼图":
        print("生成饼图");
        graph_name = "pie";
        # 准备图轨数据
        confirmed = graph_data.get("confirmed");
        outsideinput = graph_data.get("outsideinput");
        cure = graph_data.get("cure");
        death = graph_data.get("death");
        isolation = graph_data.get("isolation");
        observe = graph_data.get("observe");
        trace_1 = plotly.graph_objs.Pie(
            labels=["确诊人数", "境外输入人数", "治愈人数", "死亡人数", "隔离人数", "待观察人数"],
            values=[sum(confirmed), sum(outsideinput), sum(cure), sum(death), sum(isolation), sum(observe)]
        );
        trace_data = [trace_1];
    else:
        if graph_typle == "折线图":
            classname = "Scatter";
            graph_name = "line";
            print("生成折线图");
        elif graph_typle == "柱状图":
            classname = "Bar";
            graph_name = "bar";
            print("生成柱状图");
        # 准备图轨数据(利用反射动态获取classname)
        trace_1 = plotly.graph_objs.__getattr__(classname)(
            x=graph_data.get("time"),
            y=graph_data.get("confirmed"),
            name="确诊人数",
        );
        trace_2 = plotly.graph_objs.__getattr__(classname)(
            x=graph_data.get("time"),
            y=graph_data.get("outsideinput"),
            name="境外输入人数",
        );
        trace_3 = plotly.graph_objs.__getattr__(classname)(
            x=graph_data.get("time"),
            y=graph_data.get("cure"),
            name="治愈人数",
        );
        trace_4 = plotly.graph_objs.__getattr__(classname)(
            x=graph_data.get("time"),
            y=graph_data.get("death"),
            name="死亡人数",
        );
        trace_5 = plotly.graph_objs.__getattr__(classname)(
            x=graph_data.get("time"),
            y=graph_data.get("isolation"),
            name="隔离人数",
        );
        trace_6 = plotly.graph_objs.__getattr__(classname)(
            x=graph_data.get("time"),
            y=graph_data.get("observe"),
            name="待观察人数",
        );
        trace_data = [trace_1, trace_2, trace_3, trace_4, trace_5, trace_6];
    # 设置画面布局
    layout = plotly.graph_objs.Layout(title=district + "疫情数据_" + graph_typle, xaxis={"title": "日期"},
                                      yaxis={"title": "数量"});
    # 将图轨数据放入到布局中
    figure = plotly.graph_objs.Figure(data=trace_data, layout=layout);
    # 生成图表和图片
    filepath = "E://python_production_projects/python_graph/gzbd_" + graph_name + "_graph.html";
    plotly.offline.plot(figure_or_data=figure, filename=filepath, image="png");


if __name__ == "__main__":
    # graph_typle1 = "饼图";
    # graph_typle2 = "折线图";
    # graph_typle3 = "柱状图";
    # draw_graph(graph_typle3);
    pass;
