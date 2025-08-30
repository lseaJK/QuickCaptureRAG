use screenshots::Screen;
use std::fs;
use std::time::SystemTime;
use tauri::Manager;
use tauri_plugin_global_shortcut::{GlobalShortcut, Shortcut};

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            if cfg!(debug_assertions) {
                app.handle().plugin(
                    tauri_plugin_log::Builder::default()
                        .level(log::LevelFilter::Info)
                        .build(),
                )?;
            }

            let handle = app.handle().clone();
            let mut shortcut = Shortcut::new("CmdOrCtrl+K");
            app.handle()
                .plugin(tauri_plugin_global_shortcut::Builder::new().build())?
                .register(shortcut.clone())?;

            shortcut.on_key_down(move || {
                let screens = Screen::all().unwrap();
                let pictures_dir = handle
                    .path()
                    .picture_dir()
                    .unwrap_or_else(|| handle.path().home_dir().unwrap());
                let capture_dir = pictures_dir.join("QuickCapture");

                if !capture_dir.exists() {
                    fs::create_dir_all(&capture_dir).unwrap();
                }

                for screen in screens {
                    let image = screen.capture().unwrap();
                    let timestamp = SystemTime::now()
                        .duration_since(SystemTime::UNIX_EPOCH)
                        .unwrap()
                        .as_secs();
                    let filename = format!("capture_{}.png", timestamp);
                    let path = capture_dir.join(&filename);
                    image.save(&path).unwrap();
                    println!("Screenshot saved to: {:?}", path);
                }
            });

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}

