#!/bin/bash
# Rebuilds the Mac app from this folder.
# Usage:  tools/pack-app.sh "/Users/YOU/Desktop/Lily Path.app"
set -e
APP="$1"
[ -d "$APP/Contents/Resources" ] || { echo "Give the path to Lily Path.app"; exit 1; }
cd "$(dirname "$0")/.."
STAGE="$(mktemp -d)"
rsync -a --exclude .git --exclude archive --exclude tools --exclude supabase --exclude README.md --exclude .gitignore --exclude node_modules ./ "$STAGE/"
cp "$APP/Contents/Resources/app.asar" "$APP/Contents/Resources/app.asar.previous" 2>/dev/null || true
npx --yes @electron/asar pack "$STAGE" "$APP/Contents/Resources/app.asar"
HASH=$(node -e "
const fs=require('fs'),c=require('crypto');
const b=fs.readFileSync(process.argv[1]);const n=b.readUInt32LE(12);
console.log(c.createHash('sha256').update(b.slice(16,16+n).toString('utf8')).digest('hex'))" "$APP/Contents/Resources/app.asar")
/usr/libexec/PlistBuddy -c "Set :ElectronAsarIntegrity:Resources/app.asar:hash $HASH" "$APP/Contents/Info.plist"
echo "Done. Quit and reopen Lily Path."
