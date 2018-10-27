var gulp = require('gulp');
var electron = require('electron-connect').server.create();

gulp.task('start', function() {
  electron.start('./app')

  gulp.watch(['./app/*.js'], electron.restart);
  gulp.watch(['./app/*.{html,css}'], electron.reload)
})
