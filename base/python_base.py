import re
import math

# 导入自定义的包
# import utils.mytest
# 资源包右键->Mark Directory as->resource
# import mytest
'''
a = 12;
b = "whc";
c = "hello world";
print(a);
print(b);
print("%s %s"%(c,b));
'''

'''
a = 3.141592653591687
print("a = %s,数据类型为:%s" % (a, type(a)));
b = "sdfa";
print("b = %s,数据类型为:%s" % (b, type(b)));
c = ["aaa", "bbb", 456];
print("c = %s,数据类型为:%s" % (c, type(c)));
# NoneType
d = None;
print("d = %s,数据类型为:%s" % (d, type(d)));
# tuple
e = ("aaa", "bbb", 456);
print("e = %s,数据类型为:%s" % (e, type(e)));
# set
f = {"aaa", "bbb", 456};
print("f = %s,数据类型为:%s" % (f, type(f)));
g = True or False;
# g = 2 > 1;
# g = not False;
print("g = %s,数据类型为:%s" % (g, type(g)));
'''

'''
#运算符
print(15//6);#取整（地板除）
print(15/6);#精确值
print(15%6);#取余
print(2**3);#阶乘
'''

'''
#编码转换
print("文浩丞".encode("utf8"));
#转换为16进制
print("%x"%333);
'''

'''
#function
#len
print(len("lkasb32"));
#replace
print("kasjdbwhcfsdkabwhc".replace("whc","yyl"));
#find(返回要找的字符串的第一个字母的出现的第一次的下标，从0开始)
print("kasjdbwhcfsdkabwhc".find("whc"));#6
#rfind(返回要找的字符串的第一个字母的出现的最后一次的下标，从0开始)
print("kasjdbwhcfsdkabwhc".rfind("whc"));#15
#isspace()-->判断是否由空格组成
print("".isspace());
'''

# 字符串格式化
# print("%s %% %s" % (3, 5));
# a = list(range(1, 10));
# print(a);
# print(list("%s" % x for x in range(1, 10)));
# # 2d:不足两位左边补空格；#02d:不足两位的左边补0
# print("%d----%2d-----%02d" % (2, 3, 4));
# # %f:默认保留6位小数；%.2f保留2位小数，四舍五入
# print("%f----%.2f" % (111.111, 222.225000001));
# print("{0},你今年{1}岁了".format("小明", 24));
# print("{0},你身高是{1:.2f}m".format("小明", 1.765));
# print("_".join(["a", "b", "c"]));


'''
#函数
def A(a, b):
    total = a + b;
    print("总和为：%s"%total)
    return total;
A(1,2);
'''

# 切分字符串
# a = "sadf@sdaf@_@fgs"
# print(a.split("@"));

# -----正则表达式-->引入re-----
# . ---- 匹配任意字符；\d ---- 匹配数字；\w ---- 匹配字母；\s ---- 匹配一个空格（包含tab）；
# * ---- 任意个字符（包括0个）；+ ---- 至少一个字符；? ---- 表示0个或1个字符；{n} ---- 表示n个字符；{n,m} ---- 表示n-m个字符；
# [] ---- 表示范围 ---- [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
# () ---- 表示提取的分组，按照正则表达式拆分原始字符串，group(0)永远是原始字符串；
# A|B ---- 匹配A或B；^ ----表示行的开头；^\d ---- 表示必须以数字开头；$ ---- 表示行的结束；\d$ ---- 表示必须以数字结束；

# -----分组-----
# 分组提取电话号码
# num = re.match(r"^(\d{3})-(\d{3,8})$", "010-12345");
# print(num.groups()); # ('010', '12345')
# print(num.group(0)); # 010-12345
# print(num.group(1)); # 010
# print(num.group(2)); # 12345
# print(re.split(r"\s+", "b c d"));

# ==== 前缀字符串 ====
# print(u'中文'); # 后面字符串是以Unicode编码
# print(r'dddd'); # 后面字符串是普通字符串
# print(b'qwerr'); # 后面是bytes

# def check(str1, str2):
#     return sum(map(lambda ch: str1.count(ch), str2))


# 分组提取数字
# new = r"美国约翰斯·霍普金斯大学发布的疫情数据显示，截至北京时间6月19日6时30分左右，美国累计确诊2182285例，" \
#       r"累计死亡118296例。与前一日6时30分数据相比，美国新增确诊病例22839例，新增死亡病例633例。";
# new_line = re.compile(
#     r"^美国约翰斯·霍普金斯大学发布的疫情数据显示，截至北京时间(\d+)月(\d+)日(\d+)时(\d+)分左右，美国累计确诊(\d+)例，"
#     r"累计死亡(\d+)例。与前一日(\d+)时(\d+)分数据相比，美国新增确诊病例(\d+)例，新增死亡病例(\d+)例。$");
# # match(pattern, string)--->参数顺序不能改变
# new_line_mathc = re.match(new_line, new);
# new_len = list(range(1, 11));
# for i in new_len:
#     print(new_line_mathc.group(i));

# --------------list&tuple------------------------
# ---------list--------------
# list->有序的集合，中括号定义，元素类型可不一致，可以随时添加和删除其中的元素；
# l1 = ["one", "two", "there"];
# l2 = [1, 2, 3];
# l3 = list(range(1, 10));
# print(l3);
# l1.append(l2);
# print(l1);
# l1.insert(1, 5);
# print(l1);
# -----------tuple(元组)
# 元组-->小括号定义，有序，元素不可变
# t1 = ("aaa", "bbb", 45);
# t2 = tuple(range(1, 10));
# 当元组中只有一个元素的时候要在末尾加“，
# t3 = ("sadf",);
# print(t1);
# print(t2);


# ----dict&set----
# ------dict-------------
# 花括号定义，可变容器模型，且可存储任意类型对象，使用key-value存储，具有极快的查询速度（list逐个查找，dict索引查找）
# d1 = {"name": "whc", "age": 24};
# 通过key值来找value
# print(d1.get("name"));
# 如果在dict中没有这样的key值，可以指定返回value
# print(d1.get("height", 150));

# ------set-------------
# 小括号+中括号定义，存储的是一组key集合，不存储value，没有重复元素，自动过滤重复key，而且key也必须为不可变对象
# s1 = set(["a", True, 15, 12.5]);
# s2 = {"a", 1, 2, 15, 12.5};
# s1.add("whc");
# 用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。但是由于set是无序的，所以不能通过序号删除
# s1.pop();
# print(s1);
# 移除列表中某个值的第一个匹配项
# s1.remove("a");
# print(s1);
# 具有自动过滤掉重复的key的功能
# 交集与合集
# print(s1 & s2);
# print(s1 | s2);

# ------条件语句------
# a = 10;
# if a > 20:
#     print("aaaa");
# elif 10 < a < 20:
#     print("bbbb");
# else:
#     print("cccc");
# 三目运算符
# a,b,c = 1,2,3;
# print(a if (b>c) else c);

# -----循环语句------
# a =1;
# while a<10:
#     print(a);
#     a += 1;

# l1 = list(range(1,10));
# for a in l1:
#     print(a);

# --------内置函数-->需要引入math------
# 去除字符串前后空格
# print("aa bb cc ".strip());
# 将字符串第一个字符变成大写，其他小写
# print("myTestPython".capitalize());

# ----可变参数的函数-----
# def test_1(name, age, *my_list):
#     print("name=%s" % name);
#     print("name=%s" % age);
#     for a in my_list:
#         print("my_list_value=%d" % a);

# test_1("whc", 23, *(1, 2, 3));
# test_1("whc", 23, *list(range(1,5)));

# ----可变关键字参数
# def test_2(name, age, **fruit):
#     print("name=%s,age=%s,fruit=%s" % (name, age, fruit.get("my_favorite_fruit")));
#
#
# fruit = {"my_favorite_fruit": "banana"}
# test_2("whc", 23, **fruit);
