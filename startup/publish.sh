#Blender configure

#Version=1.0
#Type=Application
#Terminal=true
#Name[en_GB]=blender
#Exec=/home/subin/Software/blender-2.79/blender
#Name=eclipse

source /media/subin/FE5868105867C5CD/Project/MiniMovie/packages/startup/environ.sh

export PROJECT_NAME=$PROJECT_NAME
export PROJECT_PATH=$PROJECT_PATH
export PROJECT_ADMIN=$PROJECT_ADMIN

export BLENDER_VERSION=$BLENDER_VERSION
export PYTHON_VERSION=$PYTHON_VERSION

export BLENDER_PATH=$BLENDER_PATH
export PYTHON_PATH=$PYTHON_PATH
export ICON_PATH=$ICON_PATH
export IMAGE_PATH=$IMAGE_PATH
export LIBARARY_PATH=$LIBARARY_PATH
export APPLICATION_PATH=$APPLICATION_PATH
export DATABASE_PATH=$DATABASE_PATH

export PUBLISH_PATH=$PUBLISH_PATH

echo "................................................................"
echo PROJECT_NAME = $PROJECT_NAME
echo PROJECT_PATH = $PROJECT_PATH
echo BLENDER_VERSION = $BLENDER_VERSION
echo BLENDER_PATH = $BLENDER_PATH
echo "Loading Publish, please wait .............................."

#$PYTHON_PATH/python3.5 /media/subin/FE5868105867C5CD/Project/MiniMovie/packages/pipe/studioPublish.py
#./studioPublish.py /media/subin/FE5868105867C5CD/Project/MiniMovie/packages/pipe/studioPublish.py