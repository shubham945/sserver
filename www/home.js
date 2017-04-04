/**
 * Created by prajyot on 4/4/17.
 */

var app = angular.module('home',['ngCookies']);

app.controller('HomeCtrl',['$scope', '$http', '$cookies', function($scope, $http, $cookies){
    $http.get("/get-images").then(function (resp) {
        console.log(resp.data);
        $scope.imageList = resp.data;
    });
}]);