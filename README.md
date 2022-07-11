## Storehouse
An application for storing and hosting video content

### Commands
Migrations

`flask db init`

`flask db migrate`

`flask db upgrade`

### Rough description

- main page where all the available content is shown
- upload page where a registered user can upload his own video
- watch page where user can watch content
    - if it's just a video or film then it's just a page with video player and short description
    - if it's a series then there should be an episode selector

### Considering adding / giving some thought

- tags for videos
- download button
- continue watching feature
- automatically search for intro and if there is one show skip intro button (only on series)
- audio tracks selector
- quality selector

### TODO notes
- add pfps
- add video covers
- add video files
- add multiple videos to series
