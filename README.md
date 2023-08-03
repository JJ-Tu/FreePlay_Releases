# FreePlay_Releases
Checks for new FreePlay ticket drops at intermittent intervals

Currently (as of 07/03/2023) it cannot update the previous_section.txt that is used to compare to the current status of the FreePlay website. 
If/when changes happen to the FreePlay website, the script should be run on a local computer to generate an updated previous_section.txt and replace the one in this GitHub repository accordingly.

Tried a few methods to get GitHub actions to automatically update the previous_section.txt file but none have worked.
Some of these methods include:
- switch to SSH authentication instead of HTTPS in your GitHub Actions workflow
- generating a Personal Access Token (PAT) and modifying a git push command in the Actions workflow
