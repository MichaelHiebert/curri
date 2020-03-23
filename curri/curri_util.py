import json

class Course():
    def __init__(self, json_course):
        """
            Initialize the Education object.

            params
            ------
            json_course : json dictionary
                the json representation of this course

            return
            ------
            None
        """

        self._process_json(json_course)

    def _process_json(self, json_course):
        """
            Digest the json of this course.

            params
            ------
            json_course : json dictionary
                the json representation of this course

            return
            ------
            None
        """

        self.title = json_course['title']
        self.enabled = json_course['enabled']
        self.emphasized = json_course['emphasized']

    def latex(self):
        """
            A to_string() variant returning the latex representation of this course

            return
            ------
            the latex representation of this course
        """
        if self.enabled:
            if self.emphasized:
                return '\\textbf{' + self.title + '}'
            else:
                return self.title
        else:
            return ''


class Education():
    def __init__(self, json_education):
        """
            Initialize the Education object.

            params
            ------
            json_education : json dictionary
                the json representation of this education entry

            return
            ------
            None
        """

        self._process_json(json_education)

    def _process_json(self, json_edu):
        """
            Digest the json representation of an education section.

            params
            ------
            json_education : json dictionary
                the json representation of this education entry

            return
            ------
            None
        """
        self.degree = json_edu['degree']
        self.graduationDate = json_edu['graduationDate']
        self.school = json_edu['school']
        self.major = json_edu['major']
        self.misc = json_edu['misc']

        self.coursework = [self._process_course(entry) for entry in json_edu['coursework']] if len(json_edu['coursework']) > 0 else None

    def _process_course(self, course):
        """
            Digest the json representation of a course.

            params
            ------
            course : json dictionary
                the json representation of a course

            return
            ------
            A `Course` object representing this json object
        """
        return Course(course)

    def latex(self):
        """
            A to_string() variant returning the latex representation of this Education

            return
            ------
            the latex representation of this Education
        """
        latex_str = '\\textbf{' + self.degree + ' $\mid$ ' + self.graduationDate + ' $\mid$ ' + self.school + '}'

        latex_str += '\n\\small{'

        if self.major or self.misc or self.coursework: latex_str += '\\\\'

        if self.major: latex_str += '\\tabitem Major: ' + self.major + '\\\\'
        if self.misc: latex_str += '\\tabitem ' + self.misc + '\\\\'
        if self.coursework: latex_str += '\\tabitem Relevant Coursework: ' + ', '.join([x.latex() for x in self.coursework])
        latex_str += '}'

        return latex_str

class Project():
    def __init__(self, json_project):
        """
            Digest the json representation of a project.

            params
            ------
            course : json dictionary
                the json representation of a project

            return
            ------
            None
        """

        self.name = json_project['projName']
        self.args = json_project['trailingArgs'] if len(json_project['trailingArgs']) > 0 else None
        self.info = json_project['info'] if len(json_project['info']) > 0 else None

    def latex(self):
        """
            A to_string() variant returning the latex representation of this Project

            return
            ------
            the latex representation of this Project
        """

        args = [] if self.args == None else self.args

        combined_title = [self.name] + args

        latex_str = '\\textbf{' + ' $\mid$ '.join(combined_title) + '}'

        latex_str += '\n\\small{'

        if self.info:
            latex_str += '\\\\\n'
            latex_str += '\\\\'.join(['\\tabitem {}'.format(i) for i in self.info])

        latex_str += '}'

        return latex_str


class Experience():
    def __init__(self, json_exp):
        """
            Digest the json representation of a project.

            params
            ------
            course : json dictionary
                the json representation of a project

            return
            ------
            None
        """

        self.title = json_exp['jobTitle']
        self.company = json_exp['company']
        self.start = json_exp['start']
        self.end = json_exp['end']
        
        self.about = json_exp['about'] if len(json_exp['about']) > 0 else None

    def latex(self):
        """
            A to_string() variant returning the latex representation of this Experience

            return
            ------
            the latex representation of this Experience
        """

        latex_str = '\\textbf{' + ' $\mid$ '.join([self.title, self.company, '{} - {}'.format(self.start, self.end)]) + '}'

        latex_str += '\\\\\n\\small{'

        latex_str += '\\\\'.join(['\\tabitem {}'.format(i) for i in self.about])

        latex_str += '}'

        return latex_str
