$VersionControl='git'
$Package='pip'
$Build='python'

$Test='pytest'
$TestInclude='./test/'

$Deploy='none'
$Run='process'
$RunStartCommand='python'
$RunStartArguments=@('-m', 'examples.app')
