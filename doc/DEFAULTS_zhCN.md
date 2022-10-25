# 🔌 覆盖默认配置

Discord Presence Submod 包含了一套持续开发中的默认配置集，如果你想直接修改它来展现你的风格，可能会不是很方便，因为更新时你的修改都会被覆盖。
当然，你可以创建自己的配置文件，来覆盖默认设置。

例如，如果你想覆盖配置文件events/anni-year.conf，优先级为-100。
那么你创建自己的配置时，保持条件相同（或根据你的需求）并且修改优先级为-99即可覆盖配置。

## 默认配置和优先级

你可以看到一个包含默认配置文件和它们的优先级的表格。可以方便地找到你想要的配置和它的优先级，而不需要打开每一个文件。

### 话题配置

| 优先级（Priority） | 配置名（Config）                                                                  |
|----------|-------------------------------------------------------------------------|
| -20      | topics/exp-previewer.conf                                               |
| -20      | topics/floating-islands.conf                                            |

### 纪念日/里程碑配置

| 优先级（Priority） | 配置名（Config）                                                                  |
|----------|-------------------------------------------------------------------------|
| -90      | events/anni-year-day.conf                                               |
| -90      | events/anni-milestone-day.conf                                          |

### 纪念日/里程碑前一周配置

| 优先级（Priority） | 配置名（Config）                                                                  |
|----------|-------------------------------------------------------------------------|
| -100     | events/anni-year.conf                                                   |
| -100     | events/anni-milestone.conf                                              |

### 你或莫妮卡的生日的配置

| 优先级（Priority） | 配置名（Config）                                                                  |
|----------|-------------------------------------------------------------------------|
| -190     | events/player-bday-day.conf                                             |
| -190     | events/moni-bday-day.conf                                               |

### 你或莫妮卡的生日前一周的配置

| 优先级（Priority） | 配置名（Config）                                                                  |
|----------|-------------------------------------------------------------------------|
| -200     | events/player-bday.conf                                                 |
| -200     | events/moni-bday.conf                                                   |

### 在“我一会回来”的配置

| 优先级（Priority） | 配置名（Config）                                                                  |
|----------|-------------------------------------------------------------------------|
| -600     | be-right-backs/my-otter-self-brbs/stretching.conf                       |
| -600     | be-right-backs/my-otter-self-brbs/stimulation.conf                      |
| -600     | be-right-backs/my-otter-self-brbs/social.conf                           |
| -600     | be-right-backs/my-otter-self-brbs/plants.conf                           |
| -600     | be-right-backs/my-otter-self-brbs/nails.conf                            |
| -600     | be-right-backs/my-otter-self-brbs/liedown.conf                          |
| -600     | be-right-backs/my-otter-self-brbs/journal.conf                          |
| -600     | be-right-backs/my-otter-self-brbs/food.conf                             |
| -600     | be-right-backs/my-otter-self-brbs/date.conf                             |
| -600     | be-right-backs/my-otter-self-brbs/call.conf                             |
| -600     | be-right-backs/misc/radio.conf                                          |
| -600     | be-right-backs/misc/podcast.conf                                        |
| -600     | be-right-backs/misc/panic.conf                                          |
| -600     | be-right-backs/misc/overstimulated.conf                                 |
| -600     | be-right-backs/misc/listening2.conf                                     |
| -600     | be-right-backs/misc/listening.conf                                      |
| -600     | be-right-backs/misc/jamming.conf                                        |
| -600     | be-right-backs/misc/drama.conf                                          |
| -600     | be-right-backs/mas/writing.conf                                         |
| -600     | be-right-backs/mas/workout.conf                                         |
| -600     | be-right-backs/mas/working.conf                                         |
| -600     | be-right-backs/mas/showering.conf                                       |
| -600     | be-right-backs/mas/reading.conf                                         |
| -600     | be-right-backs/mas/napping.conf                                         |
| -600     | be-right-backs/mas/homework.conf                                        |
| -600     | be-right-backs/mas/generic.conf                                         |
| -600     | be-right-backs/mas/gaming.conf                                          |
| -600     | be-right-backs/mas/coding.conf                                          |
| -600     | be-right-backs/mas/break.conf                                           |
| -600     | be-right-backs/genetechnician-reading-submod/watching_movie_videos.conf |
| -600     | be-right-backs/genetechnician-reading-submod/watching_game.conf         |
| -600     | be-right-backs/genetechnician-reading-submod/watching_drawing.conf      |
| -600     | be-right-backs/genetechnician-reading-submod/watching_code.conf         |
| -600     | be-right-backs/genetechnician-reading-submod/reading_romance.conf       |
| -600     | be-right-backs/genetechnician-reading-submod/reading_misc.conf          |
| -600     | be-right-backs/genetechnician-reading-submod/reading_manga.conf         |
| -600     | be-right-backs/genetechnician-reading-submod/reading_horror.conf        |
| -600     | be-right-backs/genetechnician-reading-submod/reading_dystopian.conf     |

### 特殊日期配置

| 优先级（Priority） | 配置名（Config）                                                                  |
|----------|-------------------------------------------------------------------------|
| -790     | events/all-day.conf                                                     |

### 特殊日期前一周配置

| 优先级（Priority） | 配置名（Config）                                                                  |
|----------|-------------------------------------------------------------------------|
| -800     | events/all.conf                                                         |

### 夜间或早晨的配置

| 优先级（Priority） | 配置名（Config）                                                                  |
|----------|-------------------------------------------------------------------------|
| -950     | time-of-day/night.conf                                                  |
| -950     | time-of-day/morning.conf                                                |

### 天气配置

| 优先级（Priority） | 配置名（Config）                                                                  |
|----------|-------------------------------------------------------------------------|
| -995     | weather/thunder.conf                                                    |
| -995     | weather/snow.conf                                                       |
| -995     | weather/rain.conf                                                       |

### 默认配置

| 优先级（Priority） | 配置名（Config）                                                                  |
|----------|-------------------------------------------------------------------------|
| -1000    | default.conf                                                            |