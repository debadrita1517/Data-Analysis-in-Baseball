import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
judge=pd.read_csv('https://raw.githubusercontent.com/debadrita1517/Data-Analysis-in-Baseball/main/judge.csv')
stanton=pd.read_csv('https://raw.githubusercontent.com/debadrita1517/Data-Analysis-in-Baseball/main/stanton.csv')
pd.set_option('display.max_columns',None)
print(judge.tail(5))
judge_events_2017=judge.loc[judge['game_year']==2017].events
print("\nAron Judge's batted ball event totals, 2017 :")
print(judge_events_2017.value_counts())
stanton_events_2017=stanton.loc[stanton['game_year']==2017].events
print("\Giancarlo Stanton's batted ball event totals, 2017 :")
print(stanton_events_2017.value_counts())
judge_hr = judge[judge['events']=='home_run']
stanton_hr = stanton[stanton['events']=='home_run']
fig1, axs1 = plt.subplots(ncols=2, sharex=True, sharey=True)
sns.regplot(x='launch_angle', y='launch_speed', fit_reg=False, color='tab:blue', data=judge_hr, ax=axs1[0]).set_title('Aaron Judge\nHome Runs, 2015-2017')
sns.regplot(x='launch_angle', y='launch_speed', fit_reg=False, color='tab:blue', data=stanton_hr, ax=axs1[1]).set_title('Giancarlo Stanton\nHome Runs, 2015-2017')
fig2, axs2 = plt.subplots(ncols=2, sharex=True, sharey=True)
sns.kdeplot(judge_hr.launch_angle, judge_hr.launch_speed, cmap="Blues", shade=True, shade_lowest=False, ax=axs2[0]).set_title('Aaron Judge\nHome Runs, 2015-2017')
sns.kdeplot(stanton_hr.launch_angle, stanton_hr.launch_speed, cmap="Blues", shade=True, shade_lowest=False, ax=axs2[1]).set_title('Giancarlo Stanton\nHome Runs, 2015-2017')
judge_stanton_hr = pd.concat([judge_hr, stanton_hr])
sns.boxplot(x='player_name',y='release_speed', color='tab:blue', data=judge_stanton_hr).set_title('Home Runs, 2015-2017')
def assign_x_coord(row):
    if row.zone in [1, 4, 7]:
        return 1
    if row.zone in [2, 5, 8]:
        return 2
    if row.zone in [3, 6, 9]:
        return 3

def assign_y_coord(row):
    if row.zone in [1, 2, 3]:
        return 3
    if row.zone in [4, 5, 6]:
        return 2
    if row.zone in [7, 8, 9]:
        return 1
judge_strike_hr = judge_hr.copy().loc[judge_hr.zone <= 9]
judge_strike_hr['zone_x'] = judge_strike_hr.apply(assign_x_coord, axis=1)
judge_strike_hr['zone_y'] = judge_strike_hr.apply(assign_y_coord, axis=1)
plt.hist2d(judge_strike_hr['zone_x'], judge_strike_hr['zone_y'], bins = 3, cmap='Blues')
plt.title('Aaron Judge Home Runs on\n Pitches in the Strike Zone, 2015-2017')
plt.gca().get_xaxis().set_visible(False)
plt.gca().get_yaxis().set_visible(False)
cb = plt.colorbar()
cb.set_label('Counts in Bin')
stanton_strike_hr = stanton_hr.copy().loc[stanton_hr.zone <= 9]
stanton_strike_hr['zone_x'] = stanton_strike_hr.apply(assign_x_coord, axis=1)
stanton_strike_hr['zone_y'] = stanton_strike_hr.apply(assign_y_coord, axis=1)
plt.hist2d(stanton_strike_hr['zone_x'], stanton_strike_hr['zone_y'], bins = 3, cmap='Blues')
plt.title('Giancarlo Stanton Home Runs on\n Pitches in the Strike Zone, 2015-2017')
plt.gca().get_xaxis().set_visible(False)
plt.gca().get_yaxis().set_visible(False)
cb = plt.colorbar()
cb.set_label('Counts in Bin')
should_pitchers_be_scared = True
