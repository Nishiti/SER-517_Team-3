var createCampaignController = app.controller("createCampaignController", function ($scope, $window, $http, $location) {

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

             }, function (response) {

                 $scope.msg = "Service not Exists";

                 $scope.statusval = response.status;

                 $scope.statustext = response.statusText;

                 $scope.headers = response.headers();

             });
    }
});
