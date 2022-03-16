import pybullet as p
import time
import pybullet_data
import os
import numpy as np


def calc_ball_vel(speed: float, orient: list[float]):
    x = speed * np.sin(orient[0]) * np.cos(orient[1])
    y = speed * np.sin(orient[0]) * np.sin(orient[1])
    z = speed * np.cos(orient[0])
    return [x, y, z]


def throw_ball(ball, theta, phi, vel):
    startOrientation = p.getQuaternionFromEuler([0, 0, 0])
    p.resetBasePositionAndOrientation(
        ball, [3.5, 0, 0.3], startOrientation)
    p.resetBaseVelocity(ball,
                        calc_ball_vel(
                            vel / 3.6, [-np.pi/2 + theta * np.pi/180, phi * np.pi/180]),
                        [0, 10000, 0])


def simulation(anim=True):
    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setRealTimeSimulation(True)

    p.resetSimulation(p.RESET_USE_DEFORMABLE_WORLD)
    # Not Working
    p.resetDebugVisualizerCamera(
        cameraDistance=3,
        cameraYaw=45,
        cameraPitch=-20,
        cameraTargetPosition=[0, 0, 0])
    p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
    planeId = p.loadURDF("plane.urdf")

    # startPos = [0, 0, 1]
    bunnyId = p.loadSoftBody(
        "bunny.obj",
        [0, 0, 1],
        useNeoHookean=0,
        useBendingSprings=1,
        useMassSpring=1,
        springElasticStiffness=4,
        springDampingStiffness=3,
        springDampingAllDirections=1,
        useSelfCollision=0,
        frictionCoeff=.5,
        useFaceContact=1)
    # bunnyId2 = p.loadSoftBody(
    #     "bunny.obj",
    #     [0, 0, 3],
    #     useNeoHookean=0,
    #     useBendingSprings=1,
    #     useMassSpring=1,
    #     springElasticStiffness=4,
    #     springDampingStiffness=10,
    #     springDampingAllDirections=1,
    #     useSelfCollision=0,
    #     frictionCoeff=.5,
    #     useFaceContact=1)

    p.setGravity(0, 0, -10)

    p.changeDynamics(planeId, -1, restitution=0.8, lateralFriction=0.691)

    if anim:
        p.startStateLogging(
            p.STATE_LOGGING_VIDEO_MP4,
            os.path.join('sim.mp4'))

    for i in range(600):
        if i == 0:
            pass
        p.stepSimulation()
        time.sleep(0.01)

    if anim:
        p.stopStateLogging()
    p.disconnect()


def main():
    simulation(anim=True)
    # image = image.reshape(1800, 1800, 4)
    # img = pilimg.fromarray(image)
    # img.show()


if __name__ == "__main__":
    main()
    # time.sleep(100)
