#ifndef INCLUDED_LAUNCHER_APP_H
#define INCLUDED_LAUNCHER_APP_H
 
class LauncherApp : public wxApp
{
public:
	virtual bool OnInit();
	void Find_WoW_Path(void);
	
	wxString wow_path;
private:
	wxString Win32Registery_Find_WoW(void);
};
 
DECLARE_APP(LauncherApp)
 
#endif // INCLUDED_LAUNCHER_APP_H