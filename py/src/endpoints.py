class Endpoints:
    # Codingamer
    base = 'https://www.codingame.com/services/'
    login = base + 'Codingamer/loginSiteV2'
    getUserWithHandle = base + 'CodinGamer/findCodingamePointsStatsByHandle'
    codinGamer_followers = base + "CodinGamer/findFollowers"
    codinGamer_followers_ids = base + "CodinGamer/findFollowerIds"
    codinGamer_following = base + "CodinGamer/findFollowing"
    codinGamer_following_ids = base + "CodinGamer/findFollowingIds"
    codinGamer_coc_rank = base + "ClashOfCode/getClashRankByCodinGamerId"

    # Clash
    createClash = base + 'ClashOfCode/createPrivateClash'
    startClash = base + 'ClashOfCode/startClashByHandle'
    getClash = base + 'ClashOfCode/findClashByHandle'
    getPendingClashes = base + 'ClashOfCode/findPendingClashes'
    solution = base + "Solution/findSolution"
