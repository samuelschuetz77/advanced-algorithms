# ClassworkProfile

- **Type:** Canvas page (course policy / setup instructions, not an assignment)
- **Canvas link:** https://snow.instructure.com/courses/1254074/pages/classworkprofile?module_item_id=34811035

Referenced by every assignment: "use your non-AI-enabled Classwork Profile when writing or editing code or learning logs in this class."

## Setting up a Classwork profile in VS Code

1. Click the gear in the bottom-left of VS Code (default profile).
2. Select "Profiles" → create a new, empty profile (name it e.g. "Classwork", pick an icon like the graduation cap).
3. Click the gear again → Profiles → Classwork to switch to it.
4. To modify profile settings: click the profile icon (graduation cap) → "Settings".
5. Switch to settings.json mode (icon: paper with curved arrow) and paste:

```json
{
  "chat.disableAIFeatures": true,
  "editor.inlineSuggest.enabled": false,
  "files.autoSave": "afterDelay"
}
```
