'''
Libs included:
    underscore lodash chai sinon sinon-chai mocha async request q bluebird jsdom

    3 mice: "Mouse marathon" 26 miles
    mouse 1: runs 1 mph
    mouse 2: runs 2 mph
    mouse 3: runs 3 mph

    3 random starting points along the marathon race path
    0   ...  26

    Find the probability of which each mouse will win
    mouse 1: 40%
    mouse 2: 30%
    mouse 3: 30%

    Mouse 1 will win if
    d1 / 1mph = time it takes for mouse 1 to finish(t1)
    t1 < t2 and t1 < t3

    d1 = d2 / 2
    d1 = d3 / 3

    d3 = 26
    d1 = 26 / 3
    d2 = (26 / 3) * 2

    m3    m2    m1
    26    17.3  8.6

    t2 = d2 / 2mph
    t3 = d3 / 3mph
'''


function mouseMarathon(numRaces, mouseSpeeds) {
    const MAX_DISTANCE = 26
    const MIN_DISTANCE = 0

    const speeds = [...mouseSpeeds].sort()
    const numWins = speeds.map(speed= > 0)

    for (let i=0
         i < numRaces
         i++) {
        const positions = []
        speeds.forEach(speed=> {
            const random=(Math.random() * (MAX_DISTANCE - MIN_DISTANCE)) + MIN_DISTANCE
            positions.push(random)
        })
        positions.sort()

        const timesToFinish = speeds.map((speed, idx)=> {
            return positions[idx] / speed
        })

        let winningTime = Number.MAX_SAFE_INTEGER
        let winningIdx = -1

        timesToFinish.forEach((time, idx)=> {
            if (time < winningTime) {
                winningTime=time
                winningIdx=idx
            }
        })

        numWins[winningIdx]++
    }

    return numWins.map(wins= > (wins / numRaces) * 100)
}

console.log(mouseMarathon(100, [1, 2, 3]))
