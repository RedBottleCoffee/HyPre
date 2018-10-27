var gulp = require('gulp');
var babel = require("gulp-babel");
var electron = require('electron-connect').server.create();

var srcDir = './app/src';
var distDir = './app/dist';

gulp.task('start', ['compile'], function() {
  electron.start('./app');

  gulp.watch([srcDir + '/js/**/*.js'], ['compile']);
  gulp.watch(['./app/index.js'], electron.restart);
  gulp.watch(['./app/*.{html,css}'], electron.reload);
});

gulp.task('compile', function(){
  return gulp.src(srcDir + '/js/**/*.{js,jsx}')
    .pipe(babel())
    .pipe(gulp.dest(distDir + '/js'));
});
