from input_datas import get_data
from stdev import std
from average import ave

print('Convert your experimental data into LaTeX equations for calculating Average Value and Standard Deviation.')
print('Author: Probfia Gao (gaoh26@mail2.sysu.edu.cn, Sina Weibo @Probfia.)\n')


nums = get_data()

aveeq = ave(nums)
stdeq = std(nums)

print('\nLaTeX equation for Average is')
print('\n\\being{equation}\n' + aveeq + '\n\\end{equation}')
print('\n\nLaTeX equation for Stdev is')
print('\n\\being{equation}\n' + stdeq + '\n\\end{equation}')
