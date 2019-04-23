
var brandController = app.controller("brandController", function ($scope, $window, $http) {

    
    
    $scope.update = function() {
        console.log($scope.socialhandles);
        

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

    $scope.submitCampRequest = function() {
         var data =
                 {
                     "campaign_name" : $scope.campaignName,
                     "email" : $scope.campaignEmail,
                     "gift_campaign" : $scope.cType.value,
                     "gift_code" : $scope.gCode.value,
                     "campaign_info_rqmts" : $scope.cInfo,
                     "isApproved": false,
                     "isDenied": false
                 }

                 $http.post('http://localhost:5000/brandcampaignrequest', data).then(function (response) {

                     if (response.data)

                         console.log($scope.msg);
                         console.log("Added to the database");
                         $location.path( "/campaign" );

                 }, function (response) {

                     $scope.msg = "Service not Exists";

                     $scope.statusval = response.status;

                     $scope.statustext = response.statusText;

                     $scope.headers = response.headers();

                 });
        };

    
    
});