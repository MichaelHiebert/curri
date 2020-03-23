import json
from curri.curri_util import Education, Project, Experience

class Curri():
    def __init__(self, json_cv):
        """
            Initialize the Curri object.

            params
            ------
            json_cv : json dictionary
                the json representation of the resume
        """
        self._process_json(json_cv)
        
    def _process_json(self, json_cv):
        """
            Digest the json object for use resume generation.

            params
            ------
            json_cv : json dictionary
                the json representation of the resume
        """

        self.name = json_cv['name']
        self.address = json_cv['address']
        self.phone = json_cv['phone']
        self.email = json_cv['email']

        self.education = [self._process_education(entry) for entry in json_cv['education']] if len(json_cv['education']) > 0 else None

        self.projects = [self._process_project(entry) for entry in json_cv['projects']] if len(json_cv['projects']) > 0 else None

        self.experience = [self._process_experience(entry) for entry in json_cv['experience']] if len(json_cv['experience']) > 0 else None

        self.skills = json_cv['skills'] if len(json_cv['skills']) > 0 else None

    def _process_education(self, education_json):
        """
            Digest the json representation of an education entry.

            params
            ------
            json_cv : json dictionary
                the json representation of the education entry

            return
            ------
            Education object representing this entry
        """
        # print(education_json)
        return Education(education_json)

    def _process_project(self, project_json):
        """
            Digest the json representation of a project entry.

            params
            ------
            json_cv : json dictionary
                the json representation of the project entry

            return
            ------
            Project object representing this entry
        """
        return Project(project_json)

    def _process_experience(self, experience_json):
        """
            Digest the json representation of an experience entry.

            params
            ------
            json_cv : json dictionary
                the json representation of the experience entry

            return
            ------
            Experience object representing this entry
        """
        return Experience(experience_json)

    def latex(self):
        """
        return
        ------
        A string of the latex output for this resume.
        """

        # intro
        output = '\\documentclass{article}\n'
        output += '\\usepackage[margin=0.5in]{geometry}\n'
        output += '\\usepackage{booktabs,array,ragged2e}\n'
        output += '\\newcolumntype{P}[1]{>{\\RaggedRight\\arraybackslash}p{#1}}\n'
        output += '\\newcommand{\\tabitem}{\\textbullet~~}\n'
        output += '\\newcommand{\\specialcell}[2][c]{%\n'
        output += '\\begin{tabular}[t]{@{}p{0.8\\textwidth}@{}}#2\\end{tabular}}\n'
        output += '\\newcommand{\\tabitem}{~~\\llap{\\textbullet}~~}\n'
        output += '\\title{Michael Hiebert}\n'
        output += '\\author{' + self.address + ' | ' + self.email + ' | ' + self.phone + '}\n'
        output += '\\date{}\n'
        output += '\\begin{document}\n'
        output += '\\maketitle\n'
        output += '\\begin{tabular}{ll}\n'

        # Education
        if self.education:
            output += '\\textbf{Education} & \\specialcell{' + self.education[0].latex() + '}\\\\\n\\\\'

            for edu in self.education[1:]:
                output += '& \\specialcell{' + edu.latex() + '}\\\\\n'

        # Projects
        if self.projects:
            output += '\\\\'
            output += '\\textbf{Projects} & \\specialcell{' + self.projects[0].latex() + '}\\\\\n\\\\'

            for pro in self.projects[1:]:
                output += '& \\specialcell{' + pro.latex() + '}\\\\\n'

        # Experience
        if self.experience:
            # output += '\\\\'
            output += '\\textbf{Experience} & \\specialcell{' + self.experience[0].latex() + '}\n\\\\'

            for exp in self.experience[1:]:
                output += '\\\\& \\specialcell{' + exp.latex() + '}\n\\\\'

        # Info
        if self.skills:
            output += '\\\\\\\\'
            output += '\\textbf{Skills} & \\specialcell{ \\tabitem ' + self.skills[0] + '}\\\\\n'

            for ski in self.skills[1:]:
                output += '& \\specialcell{ \\tabitem ' + ski + '}\\\\\n'



        # wrap up latex
        output += '\\end{tabular}'
        output += '\\end{document}'

        return output

        # """
        # \documentclass{article}

        # \usepackage[margin=0.5in]{geometry}

        # \newcommand{\specialcell}[2][c]{%
        # \begin{tabular}[t]{@{}c@{}}#2\end{tabular}}

        # \begin{document}

        # \begin{itemize}
        #     \item{hi}
        #     \item ho
        # \end{itemize}

        # \begin{tabular}{@{}ll@{}}
        # \textbf{Experience} & \specialcell{Hi \\ ho}\\
        # & Did that\\
        # 4 & 6 \\
        # 7 & 9 \\
        # \end{tabular}

        # \end{document}
        # """



        