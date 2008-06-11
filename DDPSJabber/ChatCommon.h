#ifndef __CHAT_COMMON_H
#define __CHAT_COMMON_H

	#include <wx/wxprec.h>
	#ifndef WX_PRECOMP
		#include <wx/wx.h>
	#endif
	
	#include <wx/treectrl.h>
	#include <string>
	
	#include <gloox/client.h>
	#include <gloox/gloox.h>
	using namespace gloox;
	//#include "ChatMessage.h"

	//wxString LoginUsername = wxT("audiohacked");
	//wxString LoginPassword = wxT("deathball");

	enum
	{
		WINDOW_RosterList,
		TEXT_MsgText,
		BUTTON_SendMsg
	};

	std::string wx2glooxString( wxString str);
	wxString gloox2wxString( std::string str);

#endif
