# Authority
## User
UserLoginAPI = '{USERNAME}用户 登陆devEops平台'
UserCreateAPI = '{USER} 新建了新的平台用户 用户信息 用户名:{USERNAME} 名称:{FULLNAME}'
UserUpdateAPI = '{USER} 更新了平台用户信息 更新后用户信息 用户名:{USERNAME} 名称:{FULLNAME}'
UserDeleteAPI = '{USER} 删除了平台用户 删除原用户信息 用户名:{USERNAME} 名称:{FULLNAME}'
UserQRCodeAPI = '{USER} 获取了QR-CODE'
UserQRCodeAPIHaveQRCode = '当前用户已经扫描过QRCode 如有需要请联系管理员'

## PmnGroup
GroupCreateAPI = '{USER} 新建了权限组 新权限组信息 名称:{NAME}'
GroupUpdateAPI = '{USER} 更新了权限组 更新后信息 名称:{NAME}'
GroupDeleteAPI = '{USER} 删除了权限组 删除原信息 名称:{NAME}'

## Role
RoleCreateAPI = '{USER} 创建了角色 创建角色名:{NAME}'
RoleUpdateAPI = '{USER} 更新了角色 更新后角色名:{NAME}'
RoleUserAddAPI = '{USER} 新增了角色{NAME}下的用户'
RoleUserRemoveAPI = '{USER} 在角色{NAME}中删除了部分用户'
RolePageAddAPI = '{USER} 新增了角色{NAME}可操作的页面'
RolePageRemoveAPI = '{USER} 删除了角色{NAME}部分可操作的页面'
RoleAPIAddAPI = '{USER} 新增了角色{NAME}下可使用的接口'
RoleAPIRemoveAPI = '{USER} 删除了角色{NAME}下课使用的接口'

## Key
KeyCreateAPI = '{USER} 新建的密钥 密钥信息 名称:{NAME} UUID:{UUID}'
KeyUpdateAPI = '{USER} 更新了密钥 更新后密钥信息 名称:{NAME} UUID:{UUID}'
KeyDeleteAPI = '{USER} 删除了密钥 删除原密钥信息 名称:{NAME} UUID:{UUID}'
KeyDeleteAPICanNotDelete = '该密钥属于应用组{GROUP}无法删除'

## Jumper
JumperCreateAPI = '{USER} 新建了跳板机 跳板机信息 名称:{NAME} UUID:{UUID} 连接地址:{CONNECT_IP}'
JumperUpdateAPI = '{USER} 更新了跳板机 更新了跳板机信息 名称:{NAME} UUID:{UUID} 连接地址:{CONNECT_IP}'
JumperDeleteAPI = '{USER} 删除了跳板机 删除原跳板机信息 名称:{NAME} UUID:{UUID} 连接地址:{CONNECT_IP}'
JumperDeleteAPICanNotDelete = '该跳板机属于应用组{GROUP}无法删除'
JumperStatusAPI = '已进入刷新列表'

# Manager
## Group
ManagerGroupCreateAPI = '{USER} 新建了资产应用组 新建信息 名称:{NAME} UUID:{UUID}'
ManagerGroupUpdateAPI = '{USER} 更新了资产应用组 更新后信息 名称:{NAME} UUID:{UUID}'
ManagerGroupDeleteAPI = '{USER} 删除了资产应用组 删除原信息 名称:{NAME} UUID:{UUID}'
ManagerGroupDeleteAPIExsistHost = '该应用组下存在主机无法删除'
ManagerGroupSelectHostAPI = '{USER} 归类部分主机进入资产应用组 名称:{NAME} UUID:{UUID}'

## Host
ManagerHostCreateAPI = '{USER} 新建了资产主机 新建信息 主机:{HOSTNAME} 连接地址:{CONNECT_IP} UUID:{UUID}'
ManagerHostUpdateAPI = '{USER} 更新了资产主机 更新后信息 主机:{HOSTNAME} 连接地址:{CONNECT_IP} UUID:{UUID}'
ManagerHostDeleteAPI = '{USER} 删除了资产主机 删除原信息 主机:{HOSTNAME} 连接地址:{CONNECT_IP} UUID:{UUID}'
ManagerHostSelectGroupAPI = '{USER} 操作了资产主机归属 主机:{HOSTNAME} 连接地址:{CONNECT_IP} UUID:{UUID}'
ManagerHostPasswordAPI = '{USER} 获取了资产主机密码 主机:{HOSTNAME} 连接地址:{CONNECT_IP} UUID:{UUID}'
ManagerHostPasswordAPICanNotCatchPassword = '您无法获取非您管理的主机密码'
ExpireAliyunECS = '阿里云ID{aliyun_id} 资产名称{hostname} 即将过期时间{expired}'

# Ops
## META
OpsMetaCreateAPI = '{USER} 新建了元操作 新建信息 UUID:{UUID}'
OpsMetaUpdateAPI = '{USER} 更新了元操作 更新后信息 UUID:{UUID} INFO:{INFO}'
OpsMetaDeleteAPI = '{USER} 删除了元操作 删除原信息 UUID:{UUID} INFO:{INFO}'

## Mission
OpsMissionCreateAPI = '{USER} 新建了任务 新建信息 名称:{INFO} UUID:{UUID}'
OpsMissionUpdateAPI = '{USER} 更新了任务 更新后信息 名称:{INFO} UUID:{UUID}'
OpsMissionDeleteAPI = '{USER} 删除了任务 删除原信息 名称:{INFO} UUID:{UUID}'

## Quick
OpsQuickCreateAPI = '{USER} 进行了快速创建任务 任务名称:{NAME} 任务类型:{TYPE}'

# Work
## Code_Work
CodeWorkCreateAPI = '{USER} 新建了工单 工单信息 任务名称:{MISSION} 执行缘由:{REASON} UUID:{UUID}'
CodeWorkCheckAPI = '{USER} 审核了工单 工单信息 任务名称:{MISSION} 执行缘由:{REASON} UUID:{UUID}'
CodeWorkRunAPI = '{USER} 运行了工单 工单信息 任务名称:{MISSION} 执行缘由:{REASON} UUID:{UUID}'
CodeWorkUploadFileAPI = '{USER} 为工单上传文件 工单信息 任务名称:{MISSION} 执行缘由:{REASON} UUID:{UUID}'

# YoCDN
YoCDNCreateAPI = '{USER} 刷新了若干CDN信息'

# Utils

## FILE
UtilsFileCreateAPI = '{USER} 在分发中心上传了文件'
UtilsFileUpdateAPI = '{USER} 在分发中心上传了文件'
UtilsFileDeleteAPI = '{USER} 在分发中心删除了未使用的文件'

## IMAGE
UtilsImageCreateAPI = '{USER} 上传了架构图'

# Scene
## Report
SceneReportDayAPI = ''
SceneReportDayFormat = '时间{start_time}: 用户{user}本日内共操作工单{workorder_count}个，' \
                       '其中{workorder_inactive}个未激活 {workorder_run}个正在运行 {workorder_done}已经完成'

## Asset
SceneAssetChangeUpdateAPI = '{USER}修改了资产扭转中的信息 扭转的资产{UUID}'
SceneAssetChangeCreate2InstallAPI = '{USER}创建了新的资产 进入工单扭转流程 流程{UUID}'
SceneAssetChangeCreate2ConfigAPI = '{USER}配置完新创建的资产 流程{UUID}'
SceneAssetChangeCreate2DoneAPI = '{USER}完成资产信息登记 资产{UUID}生成完毕'
SceneAssetChangeUpdate2CheckAPI = '{USER}更新资产进入审核状态 流程{UUID}'
SceneAssetChangeUpdate2CheckAPILOCKED = '当前资产是无法操作状态 请将原有的资产操作流程完毕'
SceneAssetChangeUpdate2DoneAPI = '{USER}完成资产修改的审核 资产{UUID}变更完毕'
SceneAssetChangeStop2CheckAPI = '{USER}将资产{UUID}置于停止状态 审核流程扭转'
SceneAssetChangeStop2CheckAPILOCKED = '当前资产是无法操作状态 请将原有的资产操作流程完毕'
SceneAssetChangeStop2DoneAPI = '{USER}完成资产停止的审核 资产{UUID}变更完毕 已停止'
SceneAssetChangeScrap2CheckAPI = '{USER}将资产{UUID}置于废弃状态 审核流程扭转'
SceneAssetChangeScrap2CheckAPILOCKED = '当前资产是无法操作状态 请将原有的资产操作流程完毕'
SceneAssetChangeScrap2DoneAPI = '{USER}完成资产废弃的审核 资产{UUID}变更完毕 已废弃'


##
SceneWorkOrderCreateAPI = '{USER}自建新工单'
SceneWorkOrderUpdateAPI = '{USER}更新工单信息'
SceneWorkOrderActiveAPI = '{USER}激活来电工单'
SceneWorkOrderAppointAPI = '{USER1}将工单指派给{USER2}'
SceneWorkOrderDoneAPI = '{USER}完结工单'
SceneWorkOrderNotAccept = '您完结不是您负责的工单，请先转接工单。'

# EZSetup
EZSetupCreateRedisAPI = '{USER} 通过平台易装了Redis应用 安装信息 UUID:{UUID}'

# Monitor
MonitorHostAliyunDetailCPUAPI = 'CPU利用率'
MonitorHostAliyunDetailMemoryAPI = '内存使用率'
MonitorHostAliyunDetailIReadIOPS = '磁盘读取Count/Second'
MonitorHostAliyunDetailInternetInRate = '网络流入流量bits/s'
MonitorHostAliyunDetailDiskUse = '根磁盘情况'
MonitorHostAliyunDetailLoad1m = '一分钟负载'
MonitorHostAliyunDetailLoad5m = '五分钟负载'
MonitorHostAliyunDetailLoad15m = '十五分钟负载'

## ZDB
# Instance
ZDBInstanceFlushDatabaseAPI = '该实例已经进入刷新列表'

# Kalendar
KalendarCreateAPI = '{USER}用户创建了日历信息'
KalendarUpdateAPI = '{USER}用户更新了日历信息'
KalendarDeleteAPI = '{USER}用户删除了日历信息'