var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope,$http) {
    //console.log($scope.cname)

    $scope.update = function() {
        console.log($scope.socialhandles);
        console.log($scope.cname);
        console.log($scope.cname);
        console.log($scope.cname);
        console.log($scope.cname);
        console.log($scope.cname);
        console.log($scope.cname);
        console.log($scope.cname);
        console.log($scope.cname);

        var data =
        {
            "company_name" : $scope.cname,
            "email" : $scope.email,
            "password" : $scope.num,
            "address" : "tempe"
        }



        $http.post('http://localhost:5000/brand', data).then(function (response) {

            if (response.data)

                $scope.msg = "Post Data Submitted Successfully!";

        }, function (response) {

            $scope.msg = "Service not Exists";

            $scope.statusval = response.status;

            $scope.statustext = response.statusText;

            $scope.headers = response.headers();

        });

    };

});

$('.mspr').click(function(){
    console.log("hehehe")
    $(this).addClass('selected');
});





    //    .then(function(response) {  //Success

          //  $scope.content = response.data;
        //}, function(response) {     //Failure
        //    $scope.content = "Something went wrong";
        //});
