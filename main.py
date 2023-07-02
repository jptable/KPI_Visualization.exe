"""
# 產生資料，之後會有真正的資料來替代這幾組資料
"""
import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec



def randomIndustry():
    column_names = ['CPM', 'CPC', 'CTR', 'CPA']
    data = {}
    for col in column_names:
        data[col] = [random.randint(0, 100) for _ in range(10)]
    df = pd.DataFrame(data)
    return df


"""客戶資料"""
# 舊客戶資料，暫時隨機生成
# fns 是 five number summary
df = randomIndustry()

# 產生一個新客戶的資料
# fns 是 five number summary
client_df = randomIndustry()

"""Visualization"""
def create_fig(ax1_feature='CPM', ax1_stat='mean', ax2_feature='CPM', ax2_stat='mean'):
    with plt.style.context(('seaborn', 'ggplot')):
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
        plt.title='client_KPI_dashboard'
        fig = plt.figure(constrained_layout=True, figsize=(11, 4))
        specs = gridspec.GridSpec(ncols=2, nrows=3, figure=fig)
        ax1 = fig.add_subplot(specs[0, 0])
        ax2 = fig.add_subplot(specs[0, 1])

        # 訂定 x 軸, y 軸
        x = [0.8]
        x_new = [1]

        # ax1 參數
        label_ax1 = [ax1_stat]
        h_stat_func = getattr(df[ax1_feature], ax1_stat)
        h = h_stat_func()
        h_new_stat_func = getattr(client_df[ax1_feature], ax1_stat)
        h_new = h_new_stat_func()

        # ax2 參數
        label_ax2 = [ax1_stat]
        h_stat_func = getattr(df[ax2_feature], ax2_stat)
        h_ax2 = h_stat_func()
        h_new_stat_func = getattr(client_df[ax2_feature], ax2_stat)
        h_new_ax2 = h_new_stat_func()

        # 繪製橫向長條圖 ax1
        ax1.barh(x_new, h_new, height=0.2, color='c', align='edge', label='new client data')
        ax1.barh(x, h, height=0.2, color='gray',tick_label=label_ax1, label='client history')
        ax1.legend(loc='upper left', facecolor='white', framealpha=1, frameon=True)

        # 繪製橫向長條圖 ax2
        ax2.barh(x_new, h_new_ax2, height=0.2, color='c', align='edge', label='new client data')
        ax2.barh(x, h_ax2, height=0.2, color='gray',tick_label=label_ax2, label='client history')
        ax2.legend(loc='upper left', facecolor='white', framealpha=1, frameon=True)
        return fig


"""Dashboard"""
import panel as pn
import panel.widgets as pnw

pn.extension()
ax1_feature = pnw.Select(options=list(df.columns), name="選擇左圖參數")
ax1_stat = pnw.Select(options=['mean', 'min', 'max', 'median'], name="選擇左圖統計方式")
ax2_feature = pnw.Select(options=list(df.columns), name="選擇右圖參數")
ax2_stat = pnw.Select(options=['mean', 'min', 'max', 'median'], name="選擇右圖統計方式")


@pn.depends(ax1_feature.param.value,ax1_stat.param.value, ax2_feature.param.value, ax2_stat.param.value)
def create_dash(ax1_feature, ax1_stat, ax2_feature, ax2_stat):
    return create_fig(ax1_feature, ax1_stat, ax2_feature, ax2_stat)


dash = pn.Column(pn.Row(ax1_feature, ax2_feature, align='center'),
                 pn.Row(ax1_stat, ax2_stat, align='center'),
                 pn.Row(create_dash))
dash.show()

