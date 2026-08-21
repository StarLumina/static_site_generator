class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Only available in child classes")

    def props_to_html(self):
        if self.props == None:
            return ""
        
        acc = ""
        for prop in self.props:
            acc += f" {prop}=\"{self.props[prop]}\""
        return acc

    def __repr__(self):
        return f"HTMLNode( {self.tag}, {self.value}, {self.children}, {self.props_to_html()})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("all leaf nodes must have a value")
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode( {self.tag}, {self.value}, {self.props_to_html()})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("This needs a tag")
        elif self.children == None:
            raise ValueError("Cant be a parent without a child")
        container = ""
        for child in self.children:
            container += child.to_html()
        
        return f"<{self.tag}>{container}</{self.tag}>"
      
