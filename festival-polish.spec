Summary:	Basic Polish sythesizer
Summary(pl):	Prosta synteza jêzyka polskiego
Name:		festival-polish
Version:	0.1
Release:	1
License:	Non-commercial use, distributable
Group:		Applications/Sound
Source0:	ftp://voruta.ek.univ.gda.pl:21/emacspeak/festival_polish_voice.tgz
Requires:	festival
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a basic Polish synthesizer based on the work
by Dominika Oliver as part of her Masters at the Dept of Linguistics
University of Edinburgh in the summer of 1998.

%description -l pl
Ten pakiet zawiera podstawowy syntezator mowy polskiej bazuj±cy na
pracy Dominiki Oliver, bêd±cej czê¶ci± jej pracy dyplomowej z lata
1998 roku na wydziale lingwistyki Uniwersytetu w Edinburghu.

%prep
%setup -q -n cstr_pl_em_diphone

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/polish/cstr_pl_em_diphone

cp -r group festvox etc $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/polish/cstr_pl_em_diphone
find $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/polish/cstr_pl_em_diphone -name *~ -exec rm \{\} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README przeczytajto.txt
%{_datadir}/festival/lib/voices/polish
