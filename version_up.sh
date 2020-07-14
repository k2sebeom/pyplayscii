NEW_VERSION=$1
CURR_VERSION=$2

if [[ $(echo $NEW_VERSION | cut -d '.' -f 1 ) != $(echo $CURR_VERSION | cut -d '.' -f 1) ]]; then
  bumpversion major
elif [[ $(echo $NEW_VERSION | cut -d '.' -f 2 ) != $(echo $CURR_VERSION | cut -d '.' -f 2) ]]; then
  bumpversion minor
elif [[ $(echo $NEW_VERSION | cut -d '.' -f 3 ) != $(echo $CURR_VERSION | cut -d '.' -f 3) ]]; then
  bumpversion patch
fi
