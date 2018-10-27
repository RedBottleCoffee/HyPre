var gulp = require('gulp');
var sass = require('gulp-sass');
var sassGlob = require('gulp-sass-glob');
var babel = require('gulp-babel');
var electron = require('electron-connect').server.create();

var srcDir = './app/src';
var distDir = './app/dist';

gulp.task('start', ['compile'], function() {
  electron.start('./app');

  gulp.watch([srcDir + '/js/**/*.js'], ['compile']);
  gulp.watch(['./app/index.js'], () => { electron.restart('./app') });
  gulp.watch([srcDir + '/scss/*.scss'], ['sass']);
  gulp.watch([distDir + '/css/*.css'], electron.reload);
  gulp.watch(['./app/*.html'], electron.reload);
});

gulp.task('compile', function(){
  gulp.src(srcDir + '/js/**/*.{js,jsx}')
    .pipe(babel())
    .pipe(gulp.dest(distDir + '/js'));
});

gulp.task('sass', function(){
  gulp.src(srcDir + '/scss/style.scss')
    .pipe(sassGlob())
    .pipe(sass())
    .pipe(gulp.dest(distDir + '/css'));
});
